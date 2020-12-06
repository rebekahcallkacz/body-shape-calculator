# Body Shape Calculator
This script calculates body shape based on bust/waist/hip measurements. 

## Data
This analysis uses the measurements included in the Style Blogger Index. This index can be viewed at [The Median Moda](https://themedian.moda/). For the purpose of this analysis, body shapes were only calculated for entries with all three measurements in inches. Any entry missing all or part of this data was not labelled.

## Method
The formulas used to calculate body shapes were derived from [this post](https://www.whowhatwear.com/how-to-find-body-shape-calculator/slide5). You can view the function which uses the three measurements to determine body shape [here](https://github.com/rebekahcallkacz/body-shape-calculator/blob/main/shapes_calculator.py). This function was then applied to all measurements included in the Style Blogger Index in [this Jupyter Notebook](https://github.com/rebekahcallkacz/body-shape-calculator/blob/main/body_shape_calculator.ipynb). Packages used include Pandas, numpy, and matplotlib.


## Results
As you can see in the bar chart, triangles are the most common shape in the style blogger index.
![Body Shapes Bar Chart](https://github.com/rebekahcallkacz/body-shape-calculator/blob/main/bodyshapes.png "Bar Chart Body Shapes")

## Limitations
Body shape is typically calculated using a shoulder measurement instead of a bust measurement, but shoulder measurements are not included in the Style Blogger Index since this is less common measurement. If shoulder measurements had been included, it is possible that there would have been a higher percentage of inverted triangles and hourglasses in comparison to triangles.
