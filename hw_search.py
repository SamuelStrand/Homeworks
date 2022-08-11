text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu magna sit amet neque lobortis dignissim. Mauris vehicula lacinia bibendum. Phasellus elementum ipsum et mi mollis, sed eleifend elit pharetra. Donec interdum tempus ligula non vulputate. Cras mollis rhoncus facilisis. Fusce at viverra magna, id tempor nulla. Quisque at felis eget arcu gravida efficitur eget ac enim. Etiam quisque efficitur lorem at lorem dictum, a sagittis ipsum pulvinar. Maecenas elit nisi, iaculis a dolor id, tempor molestie dolor. Pellentesque aliquet non orci at convallis. Donec laoreet nisl quam. Ut accumsan, dui ut mattis ultricies, est nulla semper est, eget pulvinar magna lacus ut risus.
Duis sed hendrerit odio. Etiam scelerisque nunc quis placerat interdum. Nam condimentum enim ac justo fermentum, et imperdiet purus finibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Mauris bibendum urna vitae ullamcorper pellentesque. Aenean in est vitae felis semper vulputate convallis eu quam. Nullam feugiat elementum libero. Donec scelerisque finibus laoreet. Nam eu risus facilisis, iaculis urna vitae, aliquam neque. Donec elementum ipsum in pretium maximus.
Integer id nulla commodo elit ultricies sollicitudin vel vitae augue. Proin commodo, magna at bibendum rutrum, odio risus dictum nisi, ac commodo ipsum dolor vitae purus. Maecenas posuere, est id vulputate porta, erat lacus efficitur purus, a mattis justo ligula eu felis. Suspendisse potenti. Mauris commodo libero ut dui efficitur malesuada. Donec ultricies vel purus vel pellentesque. Etiam fusce a ex in libero rutrum placerat suscipit ac tellus. Etiam dignissim ullamcorper tincidunt. Proin tempor lorem eu nulla euismod, id sollicitudin massa ultricies."""

# переделываю строку с текстом в массив с символами
str1 = text
arr2 = []
arr1 = []
for x in str1:
    arr1.append(x)
    for char in arr1:
        arr2.append(char)

# перевожу символы всего текста в числовые значения по Юникоду и записываю их в отдельный массив
n = 0
char_arr = []

for j in arr2:
    n += 1
    value = ord(arr2[n-1])
    char_arr.append(value)
print(char_arr)
print(type(char_arr))

# сортирую массив в обратном порядке
char_arr.sort(reverse=True)
print(char_arr)

# нахожу кол-во вхождений подстроки
text = text.lower()
print(f'Кол-во вхождение слова etiam: {text.count("etiam")}')










