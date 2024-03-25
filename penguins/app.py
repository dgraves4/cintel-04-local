import plotly.express as px
from shiny import reactive
from shiny.express import input, render, ui
from shinywidgets import render_plotly
from palmerpenguins import load_penguins
import seaborn as sns

# Load penguins dataset
penguins_df = load_penguins()

# Set up the UI page options
ui.page_opts(title="Palmer Penguin Data with Dgraves4", fillable=True)

# Create the sidebar for user interaction
with ui.sidebar(open="open"):
    ui.h2("Sidebar")
    # Dropdown to select attribute
    ui.input_selectize(
        "selected_attribute",
        "Select Attribute",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    )
    # Numeric input for Plotly histogram bins
    ui.input_numeric("plotly_bin_count", "Plotly Bin Count", 30)
    # Slider for Seaborn histogram bins
    ui.input_slider(
        "seaborn_bin_count",
        "Seaborn Bin Count",
        1,
        100,
        30,
    )
    # Checkbox group for selecting species
    ui.input_checkbox_group(
        "selected_species_list",
        "Select Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie"],
        inline=True,
    )
    # Horizontal rule
    ui.hr()
    # Link to GitHub repo
    ui.a(
        "Dgraves4 on GitHub",
        href="https://github.com/dgraves4/cintel-02-data",
        target="_blank",
    )

# Layout columns for organizing content
with ui.layout_columns():
    # Data Table card
    with ui.card():
        ui.card_header("Data Table")

        @render.data_frame
        def penguin_datatable():
            return render.DataTable(penguins_df)

    # Data Grid card
    with ui.card():
        ui.card_header("Data Grid")

        @render.data_frame
        def penguin_datagrid():
            return render.DataGrid(penguins_df)


# Add a reactive calculation to filter the data
@reactive.calc
def filtered_data():
    return penguins_df[penguins_df["species"].isin(input.selected_species_list())]


# Update chart generation functions to use filtered data

# Layout columns for visualizations
with ui.layout_columns():
    # Tabbed tabset card for plots
    with ui.navset_card_tab(id="plot_tabs"):
        # Plotly Histogram tab
        with ui.nav_panel("Plotly Histogram"):

            @render_plotly
            def plotly_histogram():
                plotly_hist = px.histogram(
                    data_frame=filtered_data(),
                    x=input.selected_attribute(),
                    nbins=input.plotly_bin_count(),
                    color="species",
                ).update_layout(
                    title="Plotly Penguins Data by Attribute",
                    xaxis_title="Selected Attribute",
                    yaxis_title="Count",
                )
                return plotly_hist

        # Seaborn Histogram tab
        with ui.nav_panel("Seaborn Histogram"):

            @render.plot
            def seaborn_histogram():
                seaborn_hist = sns.histplot(
                    data=filtered_data(),
                    x=input.selected_attribute(),
                    bins=input.seaborn_bin_count(),
                )
                seaborn_hist.set_title("Seaborn Penguin Data by Attribute")
                seaborn_hist.set_xlabel("Selected Attribute")
                seaborn_hist.set_ylabel("Count")

        # Plotly Scatterplot tab
        with ui.nav_panel("Plotly Scatterplot"):

            @render_plotly
            def plotly_scatterplot():
                plotly_scatter = px.scatter(
                    filtered_data(),
                    x="bill_length_mm",
                    y="bill_depth_mm",
                    color="species",
                    size_max=8,
                    title="Plotly Scatterplot: Bill Depth and Length",
                    labels={
                        "bill_depth_mm": "Bill Depth (mm)",
                        "bill_length_mm": "Bill Length(mm)",
                    },
                )
                return plotly_scatter

        # Grouped Bar Plot tab
        with ui.nav_panel("Grouped Bar Plot"):

            @render_plotly
            def grouped_bar_plot():
                grouped_bar = px.bar(
                    filtered_data(),
                    x="island",
                    y="bill_length_mm",
                    color="species",
                    barmode="group",
                    title="Average Bill Length by Island",
                    labels={"bill_length_mm": "Average Bill Length (mm)"},
                )
                return grouped_bar
