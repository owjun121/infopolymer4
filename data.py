import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import plotly
import base64
from io import StringIO, BytesIO












# title website

st.set_page_config(page_title='INFO-POLYMER')







#Image
image = Image.open('image/image 3.png')
st.image(image,
        caption='',
        use_column_width=10
        )

#page_title
st.header('UNIVERSITY POLYTECHNIC AMU, ALIGARH')
st.subheader('POLYMER- A LIFELINE MATERIAL OF THE WORLD')
st.write('A polymer is any of a class of natural or synthetic substances composed of very large molecules',
         'called macromolecules, which are multiples of simpler chemical units called monomers.'
         'Polymers make up many of the materials in living organisms and are the basis of many minerals and man-made materials.'
)


st.subheader('PROPERTIES AND APPLICATIONS OF DIFFERENT TYPES OF POLYMER')

### --- lOAD DATAFRAME

excel_file = 'datapro.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:F',
                   header=0)

df_participants = pd.read_excel(excel_file,
                                sheet_name=sheet_name,
                                usecols='A:F',
                                header=0)


st.dataframe(df)

# download  excel_file

def generate_excel_download_link(df):

    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="POLYMER.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)

# image

image = Image.open('image/image 4.jpeg')
st.image(image,
        caption='POLYMERS',
        use_column_width=True)


# pie chart
st.subheader('PIE CHART:')

groupby_column1 = st.selectbox(
           ' What would you like to analyse? ',
           ['TENSILE STRENGTH (MPa)', 'DENSITY (gm/cm^3)', 'MELTING POINT ( ׄC)'],
           )

output_columns1 = ['NAME']
df_grouped1 = df.groupby(by=[groupby_column1], as_index=False)[output_columns1].sum( )

fig1 = px.pie(
    df_grouped1,
    values= groupby_column1,
    names='NAME',
    template='plotly_white',
    title=f'<b> NAME VS Sub-category <b>'
)
st.plotly_chart(fig1)


def generate_html_download_link(fig1):
    towrite = StringIO()
    pie_chart.write_html(towrite, include_plotlyjs="cdn",)
    towrite = BytesIO(towrite.getvalue().encode())
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:text/html;charset=utf-8;base64, {b64}"  download="pie.html">Download Pie Chart</a>'
    return st.markdown(href, unsafe_allow_html=True)



# image


image = Image.open('image/image 5.jpg')
st.image(image,
        caption='',
        use_column_width=True)




# bar chart
st.subheader('BAR CHART:')


groupby_column = st.selectbox(
           '  What would you like to analyse? ',
           ['TENSILE STRENGTH (MPa)', 'DENSITY (gm/cm^3)', 'MELTING POINT ( ׄC)'],
           )

# group dataframe
output_columns = ['NAME']
df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum( )


# plot DataFrame
fig = px.bar(
    df_grouped,
    x='NAME',
    y=groupby_column,
    color='NAME',
    color_continuous_scale=['red','yellow','green'],
    template='plotly_white',
    title=f'<b> NAME VS Sub-category <b>'
)
st.plotly_chart(fig)

#BAr chart DOWNLOAD


def generate_html_download_link(fig):
    towrite = StringIO()
    fig.write_html(towrite, include_plotlyjs="cdn")
    towrite = BytesIO(towrite.getvalue().encode())
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:text/html;charset=utf-8;base64, {b64}" download="plot.html">Download Bar/Pie Chart</a>'
    return st.markdown(href, unsafe_allow_html=True)





#DOWNLOAD

st.subheader('Downloads:')

generate_excel_download_link(df_participants)

generate_html_download_link(fig)

generate_html_download_link(fig1)




#FEEDBACK FORM

st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/owais1903114@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Details of your problem"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

#customization file name style.class



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#end

st.subheader('MADE BY:    JUNAID WARSI')
st.subheader('FACULTY NO: 20DPME328')
