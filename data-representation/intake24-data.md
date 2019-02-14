# Intake24

## <u>XML files<u/>
First we'll see different examples about how data is represented in the files.

##### xml-data/brands.xml
~~~
<brand-names>
  <food code="ALCR">
    <brand name="ASDA"/>
    .....
    <brand name="Other"/>
    <brand name="I don't know"/>
  </food>
  .....
</brand-names>
~~~


#####  xml-data/categories.xml

~~~
<categories>
  <category code="ALCL" description="Alcohol" hidden="false">
    <food code="SNOA"/>
    <subcategory code="BEER"/>
    <subcategory code="ALCO"/>
    ....
  </category>
  ...
</categories>
~~~



##### xml-data/drinkware.xml

~~~
<drinkware id="glasses_beer" description="Glasses (beer)">
		<choice guide-id="gbeer"/>
		<scale choice-id="1">
			<dimensions width="400" height="600" emptyLevel="72" fullLevel="467"/>
			<volume-function>
				<value fill="0.06666666666666667" volume="17.3"/>
				...
			</volume-function>
			<baseImage>glasses/glass1.jpg</baseImage>
			<overlayImage>glasses/glass1_fill.png</overlayImage>
    </scale>

    <scale choice-id="2">
      ...
    </scale>

    .....
</drinkware>
....

~~~


#####  xml-data/food-groups.xml

~~~
<food-groups xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:noNamespaceSchemaLocation="./Schemas/food-groups.xsd">
  <group id="0" description="Unassigned"/>
  <group id="1" description="White bread/rolls"/>
  <group id="2" description="Brown and wholemeal bread/rolls"/>
  ......
</food-groups>
~~~

#####  xml-data/foods.xml

~~~
<foods>
  <food code="AABL" description="Apple and blackcurrant squash (juice), diluted" groupCode="89">
    <nutrient-table id="NDNS" code="5501"/>
    <portion-size method="drink-scale" description="in_a_glass" imageUrl="portion/gsoftdrnk.jpg" useForRecipes="false">
      <param name="drinkware-id" value="glasses_soft"/>
      <param name="initial-fill-level" value="0.9"/>
      <param name="skip-fill-level" value="false"/>
    </portion-size>
    .......
  </food>
  .....
  <food readyMealOption="true" code="TRCP" description="Thai red curry paste " groupCode="97">
    <nutrient-table id="NDNS" code="9375"/>
    <portion-size method="guide-image" description="use_a_standard_portion" imageUrl="portion/Gspn.jpg" useForRecipes="false">
      <param name="guide-image-id" value="Gspn"/>
    </portion-size>
    ....
  </food>
  ...
</foods>
~~~

#####  xml-data/guide.xml

~~~
<guide-images xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:noNamespaceSchemaLocation="./Schemas/guide.xsd">
  <guide-image id="Gallcans" description="No description">
    <weight id="1" description="Morrisons new potatoes" value="360.0"/>
    <weight id="2" description="Heinz Farmers Market soup" value="400.0"/>
    <weight id="3" description="Heinz Big soup" value="500.0"/>
    <weight id="4" description="Weight Watchers soup" value="295.0"/>
    <weight id="5" description="Cirio plum tomatoes" value="400.0"/>
    <weight id="6" description="Batchelors Bigga peas" value="180.0"/>
    <weight id="7" description="D'aucy sweetcorn &amp; peas" value="300.0"/>
    <weight id="8" description="Morrisons mandarin segments" value="175.0"/>
    <weight id="9" description="Morrisons sweetcorn" value="140.0"/>
    <weight id="10" description="Nestle Tip Top" value="160.0"/>
    <weight id="11" description="Dole pineapple" value="227.0"/>
    <weight id="12" description="Morrisons mushy peas" value="145.0"/>
  </guide-image>

</guide-images>
~~~


##### xml-data/index_exclude
Not useful at this moment. It includes symbols that we don't take into account at this moment. Example: `and`

##### xml-data/index_filter

Not useful at this moment. It includes symbols that we don't take into account at this moment. Example: `.`

#####  xml-data/split_list
A list of food items like `cheese tomato`, `chocolate nut nuts` and so on.

#####  xml-data/synsets
~~~
cola pepsi coke
sandwich bap butty panini piece roll sarnie softie sub toastie wrap
~~~

## <u>Database<u/>

- Food Code
- Name
- Food Category
- Base Value
- Sub Group Code
- Validation Error
- Validation Overridden
- Description
- Dilution
- Max Weight
- Comment
- Edible Portion
- Deleted Food Flag
- Water
- Estimate
- Total nitrogen
- Estimate
- Nitrogen conversion factor
- Estimate
- Protein
- Estimate
- Fat
- Estimate
- Carbohydrate
- Estimate
- Energy (kcal)
- Estimate
- Energy (kJ)
- Estimate
- Alcohol
- Estimate
- Englyst fibre
- Estimate
- Southgate fibre
- Estimate
- Starch
- Estimate
- Total sugars
- Estimate
- Non-milk extrinsic sugars
- Estimate
- Intrinsic and milk sugars
- Estimate
- Glucose
- Estimate
- Fructose
- Estimate
- Sucrose
- Estimate
- Maltose
- Estimate
- Lactose
- Estimate
- Other sugars
- Estimate
- Satd FA
- Estimate
- Cis-Mon FA
- Estimate
- Cis-n3 FA
- Estimate
- Cis-n6 FA
- Estimate
- Trans FA
- Estimate
- Cholesterol
- Estimate
- Retinol
- Estimate
- Total carotene
- Estimate
- Alpha-carotene
- Estimate
- Beta-carotene
- Estimate
- Beta cryptoxanthin
- Estimate
- Vitamin A
- Estimate
- Vitamin D
- Estimate
- Thiamin
- Estimate
- Riboflavin
- Estimate
- Niacin
- Estimate
- Tryptophan/60
- Estimate
- Niacin equivalent
- Estimate
- Vitamin C
- Estimate
- Vitamin E
- Estimate
- Vitamin B6
- Estimate
- Vitamin B12
- Estimate
- Folate
- Estimate
- Pantothenic acid
- Estimate
- Biotin
- Estimate
- Sodium
- Estimate
- Potassium
- Estimate
- Calcium
- Estimate
- Magnesium
- Estimate
- Phosphorus
- Estimate
- Iron
- Estimate
- Haem iron
- Estimate
- Non-haem iron
- Estimate
- Copper
- Estimate
- Zinc
- Estimate
- Chloride
- Estimate
- Iodine
- Estimate
- Manganese
- Estimate
- Selenium
- Estimate
