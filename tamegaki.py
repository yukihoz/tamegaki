import streamlit as st

st.markdown('''
    <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/ fb# prefix属性: http://ogp.me/ns/ prefix属性#">
    <meta property="og:url" content="https://twitter.com/ninofku" />
    <meta property="og:type" content=" ページの種類" />
    <meta property="og:title" content=" ページの タイトル" />
    <meta property="og:description" content=" ページのディスクリプション" />
    <meta property="og:site_name" content="サイト名" />
    <meta property="og:image" content="tamegaki2.png" />
''',
        unsafe_allow_html=True
)

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open(r"tamegaki.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Corporate-Logo-Bold-ver2.otf", 40)


input = st.text_input('応援メッセージを入れてね', '頑張ってね！！')

draw.text((50,650), input ,(75,75,75),font=font)

img.save(r'tamegaki2.png')
 
st.image('tamegaki2.png')

st.markdown('''
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:site" content="@ninofku" />
    <meta name="twitter:title" content="(3)ページのタイトル" />
    <meta name="twitter:description" content="(4)ページの説明文" />
    <meta name="twitter:image" content="tamegaki2.png" />
''',
        unsafe_allow_html=True
)

st.markdown('''
    <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-url="http://www.example.com/" data-show-count="false">Tweet</a>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    ''',
        unsafe_allow_html=True
)



st.markdown('''
    <a href="https://twitter.com/intent/tweet?text=フローレンスつまずいてるイラスト%20https://florence.or.jp%20pic.twitter.com/FQ5xUkhaAAAJBIC%20@nomarktanaka" target="_blank">この画像をツイートする</a>
    ''',
        unsafe_allow_html=True
)


st.markdown('''
    <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
''',
        unsafe_allow_html=True
)

