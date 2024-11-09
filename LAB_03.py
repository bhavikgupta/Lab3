import geopandas as gpd

# Load the GeoJson file into a GeoDataFrame
gdf = gpd.read_file(r"C:\Users\aniqb\OneDrive\Desktop\GIS_SCRIPTS\data.txt")

print("---------Header---------")
print(gdf.head())

print("---------Columns---------")
# view the column names
print(gdf.columns)

print("---------Shape---------")
# view the shape of the GeoDataFrame
print(gdf.shape)

print("---------Data Types---------")
# view the data type of each column
print(gdf.dtypes)


#Convert the Geographic cordinates to Projected for Area Calculation
gdf = gdf.to_crs("EPSG:26914")


class CensusTract:
    """
    A class to represent a census tract.

    Attributes:
    ----------
    geoid : str
        Unique identifier for the census tract.
    population : int
        Population of the census tract.
    geometry : shapely.geometry.polygon.Polygon
        Polygon geometry of the census tract, representing its area.

    Methods:
    -------
    calculate_population_density():
        Calculates and returns the population density of the census tract based on area.
    """
    def __init__(self, geoid, population, geometry):
        """
        Constructs all the necessary attributes for the CensusTract object.

        Parameters:
        ----------
        geoid : str
            Unique identifier for the census tract.
        population : int
            Population of the census tract.
        geometry : shapely.geometry.polygon.Polygon
            Polygon geometry of the census tract, representing its area.
        """
        self.geoid = geoid
        self.population = population
        self.geometry = geometry
    
    def calculate_population_density(self):
        """
        Calculates the population density based on the geometry's area.

        Returns:
        -------
        float
            Population density in people per square kilometer.
        """
        
        # calculate the population density based on geometry
        ### >>>>>>>>>>>> YOUR CODE HERE <<<<<<<<<<< ###
        
        # Calculate area in square kilometers
        area_km2 = self.geometry.area / 1e6  # Convert from m² to km²
        # Calculate population density
        population_density = self.population / area_km2
        return population_density

        ### <<<<<<<<<<< END OF YOUR CODE <<<<<<<<<<< ###
        
        
## Task 2. Calculate the Population Density for Each Census Tract

##Now you have finished the `CensusTract` class, you can use it to calculate the population density for each census tract (each row of the original dataset). Then add the calculated population density to a new column in the `GeoDataFrame`.

# Function to apply the CensusTract class to each row
def calculate_density(row):
    """
    Applies the CensusTract class to calculate the population density for a given row.

    Parameters:
    ----------
    row : pandas.Series
        A row from the GeoDataFrame containing the census tract information.

    Returns:
    -------
    float
        Calculated population density for the census tract.
    """
    tract = CensusTract(row['GeoId'], row['Pop'], row['geometry'])
    return tract.calculate_population_density()

# Apply the function to each row and add a new column 'Population Density'
gdf['Population Density'] = gdf.apply(calculate_density, axis=1)

# Preview the data with the new column
print(gdf.head())



