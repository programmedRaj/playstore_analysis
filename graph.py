import matplotlib.pyplot as plt
import io
import base64
import seaborn as sns
 
def build_graph(x,y,y_label,x_label,title,color,ax):
    img = io.BytesIO()
    list_1 = ['Category', 'Installs', 'Type',
        'Content Rating']
    bar = sns.barplot(x = x,y=y,ax=ax,orient='h')
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    for i, v in enumerate(x.values):
        ax.text(v + 3, i + .25, str(v), color='black', fontweight='bold')
    return bar
    return 'data:image/png;base64,{}'.format(graph_url)	