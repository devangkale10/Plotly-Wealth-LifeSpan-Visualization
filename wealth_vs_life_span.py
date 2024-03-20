import numpy as np
import pandas as pd
import plotly.express as px

gapminder_df = px.data.gapminder()
gapminder_df

px.scatter(
    data_frame=gapminder_df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    title="Life Span and Wealth: 1952 - 2007",
    labels={"gdpPercap": "Wealth", "lifeExp": "Life Span"},
    log_x=True,
    range_y=[25, 95],
    hover_name="country",
    animation_frame="year",
    height=600,
    size_max=100,
)
