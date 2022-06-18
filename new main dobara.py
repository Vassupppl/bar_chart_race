import bar_chart_race as bcr
import pandas as pd

df = pd.read_csv("odi_runs1.csv", index_col="Year")

# replace empty values with 0
df.fillna(0.0, inplace=True)

# using the bar_chart_race package
bcr.bar_chart_race(
    # must be a DataFrame where each row represents a single period of time.
    df=df,

    # name of the video file
    filename="odi1.mp4",

    # specify location of image folder
    img_label_folder="bar_image_labels",
    tick_image_mode="trailing",

    # change the Figure properties
    fig_kwargs={
        'figsize': (30, 15),
        'dpi': 120,
        'facecolor': '#F8FAFF'
    },

    # orientation of the bar: h or v
    orientation="h",

    # sort the bar for each period
    sort="desc",

    # number of bars to display in each frame
    n_bars=10,

    # to fix the maximum value of the axis
    # fixed_max=True,

    # smoothness of the animation
    steps_per_period=50,

    # time period in ms for each row
    period_length=3000,


    # custom set of colors
    colors=['#80deea', '#ffee58', '#ffee58', '#ffee58', '#80deea', '#80deea', '#ffee58', '#80deea', '#ffee58', '#ffee58',
            '#80deea', '#80deea', '#ffee58', '#ffee58', '#80deea', '#b71c1c', '#80deea', '#80deea', '#546e7a', '#546e7a',
            '#2e7d32', '#b71c1c', '#b71c1c', '#b71c1c', '#546e7a', '#2e7d32', '#b71c1c', '#80deea', '#b71c1c', '#ffee58',
            '#ffee58', '#ffee58', '#80deea', '#2e7d32', '#1e88e5', '#1e88e5', '#80deea', '#1e88e5', '#546e7a', '#b71c1c',
            '#ffee58', '#ffee58', '#2e7d32', '#2e7d32', '#ffee58', '#1e88e5', '#311b92', '#311b92', '#1e88e5', '#ffee58',
            '#2e7d32', '#2e7d32', '#ffee58', '#311b92', '#1e88e5', '#b71c1c', '#1e88e5', '#ffee58', '#9ccc65', '#ffee58',
            '#2e7d32', '#311b92', '#311b92', '#1e88e5'],

    # title and its styles
    title={'label': 'Most Runs Scored in ODIs 1971-2022',
           'family': 'Helvetica',
           'size': 52,
           'weight': 'bold',
           'pad': 40
           },

    # adjust the position and style of the period label
    period_label={'x': .95, 'y': .15,
                  'ha': 'right',
                  'va': 'center',
                  'family': 'Helvetica',
                  'size': 72,
                  'weight': 'semibold'
                  },

    # style the bar label text
    bar_label_font={'family': 'Helvetica', 'size': 27},

    # style the labels in x and y axis
    tick_label_font={'family': 'Helvetica', 'weight': 'bold', 'size': 32},

    # adjust the style of bar
    # alpha is opacity of bar
    # ls - width of edge
    bar_kwargs={'alpha': .95, 'lw': 0},

    # adjust the bar label format
    bar_texttemplate='{x:.2f}',

    # adjust the period label format
    period_template='{x:.0f}',
)