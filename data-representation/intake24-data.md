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
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Total nitrogen
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Nitrogen conversion factor
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Protein
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Fat
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Carbohydrate
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Energy (kcal)
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Energy (kJ)
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Alcohol
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Englyst fibre
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Southgate fibre
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Starch
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Total sugars
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Non-milk extrinsic sugars
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Intrinsic and milk sugars
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Glucose
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Fructose
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Sucrose
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Maltose
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Lactose
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Other sugars
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Satd FA
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Cis-Mon FA
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Cis-n3 FA
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Cis-n6 FA
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Trans FA
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Cholesterol
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Retinol
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Total carotene
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Alpha-carotene
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Beta-carotene
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Beta cryptoxanthin
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Vitamin A
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Vitamin D
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Thiamin
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Riboflavin
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Niacin
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Tryptophan/60
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Niacin equivalent
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Vitamin C
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Vitamin E
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Vitamin B6
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Vitamin B12
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Folate
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Pantothenic acid
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Biotin
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Sodium
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Potassium
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Calcium
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Magnesium
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Phosphorus
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Iron
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Haem iron
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Non-haem iron
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Copper
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Zinc
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Chloride
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Iodine
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Manganese
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
- Selenium
- Estimate (yes/no and sometimes the value is in this column instead of the prior attribute in the table)
