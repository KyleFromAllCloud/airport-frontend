import streamlit as st
import subprocess

# AWS CLI configuration
aws_profile = "your_aws_profile"
aws_region = "your_aws_region"

# Streamlit app
st.title("AWS CLI Caller")

# Accept freeform text input
user_input = st.text_area("Enter AWS CLI Command:")

if st.button("Run AWS CLI Command"):
    # Validate input
    if not user_input:
        st.error("Please enter an AWS CLI command.")
    else:
        try:
            # Run AWS CLI command
            result = subprocess.run(
                ["aws", "--profile", aws_profile, "--region", aws_region] + user_input.split(),
                capture_output=True,
                text=True,
            )

            # Display the result
            st.subheader("AWS CLI Output:")
            st.code(result.stdout)

            # Display errors, if any
            if result.stderr:
                st.error(result.stderr)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
