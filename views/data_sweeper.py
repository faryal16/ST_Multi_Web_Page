import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up our page
 
st.title("📀 Data Sweeper")
st.write("Transform your files between CSV and Excel forms with built-in data cleaning and visualizations.✨")

uploaded_files = st.file_uploader(
    "📂 Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        file_name = file.name  # Ensure it's a string
        file_ext = os.path.splitext(file_name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file, engine="openpyxl")  # Ensure openpyxl is used for Excel
        else:
            st.error(f"🚫 Unsupported file type: {file_ext}")
            continue  # Skip to the next file if unsupported

        # Display file info
        st.subheader("📁 File Information")
        st.write(f"**📜 File Name:** {file_name}")
        st.write(f"**📏 File Size:** {file.getbuffer().nbytes / 1024:.2f} KB")

        # Show 5 rows of our dataframe
        st.write("👀 **Preview of the Data**")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader(f"🧹 Data Cleaning Options for {file_name}")
        if st.checkbox(f"✨ Clean Data for {file_name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"🗑️ Remove Duplicates from {file_name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("✅ Duplicates Removed")

            with col2:
                if st.button(f"🩹 Fill Missing Values for {file_name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("✅ Missing Values Filled with Column Mean")

        # Choose specific columns to keep or convert
        st.subheader("🎯 Select Columns to Convert")
        columns = st.multiselect(f"📌 Choose Columns for {file_name}", df.columns, default=df.columns)
        df = df[columns]

        # Create Some Visualizations
        st.subheader("📊 Data Visualization")

        if st.checkbox(f"📉 Show Visualization for {file_name}"):
            numeric_cols = df.select_dtypes(include=["number"]).columns

            if numeric_cols.empty:
                st.warning("⚠️ No numeric columns found. Cannot generate a visualization.")
            elif len(numeric_cols) >= 2:
                st.bar_chart(df[numeric_cols].iloc[:, :2])  # Select first two numeric columns
            else:
                st.warning(f"⚠️ Only {len(numeric_cols)} numeric column(s) found. Need at least 2 for visualization.")

        # Convert the Files --> CSV to Excel
        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        # ✅ Ensure buffer and mime_type are always defined
        buffer = BytesIO()
        mime_type = "text/csv"  # Default MIME type

        if st.button(f"Convert {file.name}"):
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False, engine="openpyxl")
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            
            buffer.seek(0)  # Move to the beginning of the buffer

        # ✅ Ensure buffer is passed correctly to download button
        st.download_button(
            label=f"📥 Download {file_name} as {conversion_type}",
            data=buffer,
            file_name=file_name,
            mime=mime_type
        )

        st.success("🎉 All files processed successfully!")
