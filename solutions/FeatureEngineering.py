elements[elements.tag == 'span'].sort(['w'], ascending=[0]).iloc[0]

elements['aspect'] = elements['h'] / elements['w']
elements.head()

elements.groupby('tag').sum().sort('area')['area'].plot(kind='barh')

elements.groupby('tag').sum().sort('aspect')['aspect'].plot(kind='barh')

# Corpa
D = []
labels = []

for page in pages[1:4]:
    page_elements = pd.DataFrame(page['elements'])
    page_elements['area'] = elements['h'] * elements['w']
    page_elements['area'].fillna(0, inplace=True)
    D.append(page_elements.groupby('tag').sum().sort('area')['area'].to_dict())
    if 'sears' in page['url']:
        labels.append('non-product')
    else:
        labels.append('product')

# Holdback
holdback = elements.groupby('tag').sum().sort('area')['area'].to_dict()

# Classifier
v = DictVectorizer()
X = v.fit_transform(D)

clf = svm.SVC(kernel="rbf", gamma=0.1)
clf.fit(X, labels)

clf.predict(v.transform(holdback))[0]        
