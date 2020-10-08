import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy as sa
from shapely import wkt




# Press the green button in the gutter to run the script.


def funcion():
   #fdf = gpd.read_file("d:/data/geopandas/espania/espania.shp")
    #df.to_csv("d:/data/geopandas/espania/espania.csv")



    engine = sa.create_engine("mssql+pyodbc://apolo/nw?driver=SQL Server?Trusted_Connection=yes")

    sql = "select cp.cp, division,nemonico, es.geometry " + \
    " from nw.dbo.tb_cp_por_plaza cp " + \
    " inner join nw.dbo.espania es on es.cp COLLATE Modern_Spanish_CI_AS = cp.cp COLLATE Modern_Spanish_CI_AS" + \
    " where pais = 'ES'  "



    data = pd.read_sql(sql, engine)
    data['geometry'] = data['geometry'].apply(wkt.loads)

    cps = gpd.GeoDataFrame(data,  geometry="geometry")

    divisiones = cps.dissolve(by='division')



    cps.plot(column="division", cmap='cividis')





    divisiones.plot()
    plt.show()



    #ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
    #plt.show()



if __name__ == '__main__':
    funcion()
