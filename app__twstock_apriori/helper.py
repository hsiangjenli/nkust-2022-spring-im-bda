import numpy as np
from pyvis.network import Network


support = 0.15
confidence = 0.8
len = 2

def RiseAndFallLoc(df):

    rise_loc = []
    fall_loc = []

    categorys = ['tw_stock_news', 'tw_macro', 'tw_quo']
    categorys_loc = []
    
    for cat in categorys:
        categorys_loc.extend(np.where(df.Category==cat))
    
    for i, context in enumerate(df['Context']):
        if '上漲' in context:
            rise_loc.append(i)
        if '下跌' in context:
            fall_loc.append(i)
    
    return rise_loc, fall_loc

def toList(x):
    return [e[0] for e in x]

def cleanRule(outputs):
    Source = []
    Target = []
    Weight = []

    for product in outputs:
        try:
            s = eval(str(product[2][0][1]))
            t = eval(str(product[2][0][0]))
            Source.append(s)
            Target.append(t)
            Weight.append(1)
        except:
            pass
    
    return Source, Target, Weight

def frozenset(x):
    return ''.join(x)

def plotNetwork(Source, Target, Weight, fname):
    got_net = Network(height='700px', width='100%', bgcolor='#d3d3d3', font_color='#3B3B3B')

    sources = Source
    targets = Target
    weights = Weight

    edge_data = zip(sources, targets, weights)

    for e in edge_data:
        src = e[0]
        dst = e[1]
        w = e[2]

        got_net.add_node(src, src, title=src, color='#C0AA7A', borderWidth=0, size=40)
        got_net.add_node(dst, dst, title=dst, color='#F8F9FA', borderWidth=0, size=20)
        got_net.add_edge(src, dst, value=w)

    neighbor_map = got_net.get_adj_list()

    # add neighbor data to node hover data
    for node in got_net.nodes:
        node['title'] += ' → ' +  ' '.join(neighbor_map[node['id']])
        # node['value'] = len(neighbor_map[node['id']])

    got_net.save_graph(f'app__twstock_apriori/templates/app__twstock_apriori/{fname}.html')