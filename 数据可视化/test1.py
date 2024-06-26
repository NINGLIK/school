import pandas as pd
from pyecharts.charts import Boxplot
import pandas as pd
import numpy as np
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Scatter3D
player_data=pd.read_excel('')
player_data=[player_data[''],player_data[''],player_data['']]
player_data=np.array(player_data).T.tolist()
s=(Scatter3D()
    .add('',player_data,xaxis3d_opts=opts.Axis3DOpts(name=''),
    yaxis3d_opts=opts.Axis3DOpts(name=''),
    zaxis3d_opts=opts.Axis3DOpts(name=''))
    .set_global_opts(title_opts=opts.TitleOpts(
        title=''),
        visualmap_opts=opts.VisualMapOpts(range_color=['#','#','#','#','#','#','#']),
    ))
s.render_notebook()