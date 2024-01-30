import streamlit as st
import subprocess
import boto3

# AWS CLI configuration
aws_access_key_id = st.secrets["aws_access_key_id"]
aws_secret_access_key = st.secrets["aws_secret_access_key"]
aws_region = "us-east-1"

# Streamlit app
st.title("Lex Intent Modifier")

# Accept freeform text input
user_input = st.text_area("Enter Intent Name:")

if st.button("Run AWS CLI Command"):
    # Validate input
    if not user_input:
        st.error("Please enter an Intent Name.")
    else:
        try:
            # Create an S3 client using boto3 with the loaded credentials
            session = boto3.client(
                'lexv2-models',
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                region_name=aws_region
            )

            # List objects in the specified S3 bucket
            objects = session.list_intents(
                botId='7LIOJYDHIB',
                botVersion='DRAFT',
                localeId='en_US'
                )

            # Display the result
            st.subheader("Objects in S3 Bucket:")
            if "Contents" in objects:
                for obj in objects["Contents"]:
                    st.write(obj["Key"])
            else:
                st.write("No objects found in the specified bucket.")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
