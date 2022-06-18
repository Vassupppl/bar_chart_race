import bar_chart_race as bcr
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("a.csv", index_col="Year")

# replace empty values with 0
df.fillna(0.0, inplace=True)

#custom vartical bar colum configuration
fig, ax = plt.subplots(figsize=(16, 10), dpi=120)
ax.set_facecolor((0, 0, 1, .3))

# using the bar_chart_race package
bcr.bar_chart_race(
    # must be a DataFrame where each row represents a single period of time.
    df=df[:5],

    # name of the video file
    filename="sector.mp4",

    # specify location of image folder
    #img_label_folder="bar_image_labels",
    #tick_image_mode="trailing",

    # change the Figure properties
    fig_kwargs={
        'figsize': (30, 15),
        'dpi': 120,
        'facecolor': '#F8FAFF'
    },

    #changes vertical bar column color
    fig = fig,

    # orientation of the bar: h or v
    orientation="h",

    # sort the bar for each period
    sort="desc",

    # number of bars to display in each frame
    n_bars=5,

    # to fix the maximum value of the axis
    # fixed_max=True,

    # smoothness of the animation
    steps_per_period=30,

    # time period in ms for each row
    period_length=500,


    # custom set of colors
    colors='dark24',

    # title and its styles
    title={'label': 'GDP per Capita of Indian States 2004-2020',
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
                  'weight': 'semibold',
                  },

    # style the bar label text
    bar_label_font={'family': 'Helvetica', 'size': 27},

    # style the labels in x and y axis
    tick_label_font={'family': 'Helvetica', 'weight': 'bold', 'size': 32},

    # adjust the style of bar
    # alpha is opacity of bar
    # ls - width of edge
    bar_kwargs={'alpha': .99, 'lw': 0},

    # adjust the bar label format
    bar_texttemplate='{x:.2f}',

    # adjust the period label format
    period_template='{x:.0f}',

)
