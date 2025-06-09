import plotly.express as px
import streamlit as st


def display_pie_chart(dset, column_to_count, column_counts):
    """Display the statistics for a given column."""
    dset_stats = (
        dset[column_to_count]
        .value_counts()
        .to_frame(name=column_counts)
        .rename_axis(column_to_count)
    )
    # change width of the table
    st.dataframe(dset_stats.style.set_table_attributes('style="width: 100%;"'))

    fig = px.pie(
        dset_stats.reset_index(),
        values=column_counts,
        names=column_to_count,
        title="",
    )
    fig.update_traces(textinfo="percent+label")
    # label with index column
    fig.update_traces(textposition="inside", textinfo="percent+label")
    st.plotly_chart(fig)


def display_bar_chart(dset, column_to_count, column_counts):
    dset_stats = (
        dset[column_to_count]
        .value_counts()
        .to_frame(name=column_counts)
        .rename_axis(column_to_count)
    )
    # change width of the table
    st.write(dset_stats.style.set_table_attributes('style="width: 100%;"'))
    fig = px.bar(
        dset_stats.reset_index(),
        x=column_to_count,
        y=column_counts,
        title="",
    )
    fig.update_traces(marker=dict(line=dict(width=0)))
    st.plotly_chart(fig)


def display_histogram(
    dset, column_to_count, column_counts, bin_width=None, color_col=None
):
    dset_stats = (
        dset[column_to_count]
        .value_counts()
        .to_frame(name=column_counts)
        .rename_axis(column_to_count)
    )

    fig = px.histogram(
        dset_stats.reset_index(),
        x=column_to_count,
        y=column_counts,
        title="",
    )
    fig.update_traces(marker=dict(line=dict(width=0)))
    st.plotly_chart(fig)


def display_bar_plot_with_colour(dset, column_to_count, column_counts, color_col):
    dset_stats = (
        dset.loc[:, [column_to_count, color_col]]
        .value_counts()
        .to_frame(name=column_counts)
        .rename_axis([column_to_count, color_col])
    )

    fig = px.bar(
        dset_stats.reset_index(),
        x=column_to_count,
        y=column_counts,
        color=color_col,
        title="",
    )
    fig.update_traces(marker=dict(line=dict(width=0)))
    st.plotly_chart(fig)


def display_cumulative_plot(dset, column_to_cuml, column_counts, colour_col):
    # Create a cumulative sum of the counts
    cuml_name = "Cumulative"
    dset_cuml = (
        dset.loc[:, [column_to_cuml, colour_col]]
        .groupby([column_to_cuml, colour_col])
        .value_counts()
        .to_frame(name=column_counts)
        .sort_index()
    )

    dset_cuml[cuml_name] = dset_cuml.groupby(level=0).cumsum()
    dset_cuml = dset_cuml.sort_values(by=[column_to_cuml])

    st.dataframe(
        dset_cuml.reset_index().style.set_table_attributes('style="width: 100%;"')
    )

    fig = px.line(
        dset_cuml.reset_index(),
        x=column_to_cuml,
        y=cuml_name,
        color=colour_col,
        title="",
    )
    st.plotly_chart(fig)

    # column_name = f"{event.capitalize()}s"
    # index_name = "Date"
    # stat = makestat(sdset, f"{event}_date", column_name, index_name)
    # stat[cuml_name] = stat[column_name].cumsum(skipna=True)
    # plt.plot(stat[cuml_name], label=f"{event.capitalize()}s")

    # stat = makestat(sdset, "referral_date", column_name, index_name)
    # stat[cuml_name] = stat[column_name].cumsum(skipna=True)
    # plt.plot(stat[cuml_name], label="Referrals")
    # plt.xticks(plt.xticks()[0], rotation=45, horizontalalignment="right", fontsize=5)
    # plt.xlabel("Date")
    # plt.legend()
    # plt.show()

