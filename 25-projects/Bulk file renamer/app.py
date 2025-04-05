import os
import streamlit as st
import tempfile
import shutil

# Function to rename files in a folder
def rename_files(directory, name_pattern, file_extension):
    files = [f for f in os.listdir(directory) if f.endswith(file_extension)]
    for i, file in enumerate(files):
        old_name = os.path.join(directory, file)
        new_name = os.path.join(directory, f"{name_pattern}_{i+1}{file_extension}")



  # Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-fj8XVTMQ7FTy3E4bv-HMcGqaBlW0e3EHQw&s");
        background-size: cover;
        background-position: center;
    }       
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .word-display {
        font-size: 2.5rem;
        letter-spacing: 0.5rem;
        font-family: monospace;
    }
    .game-title {
        color: #2c3e50;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 2rem;
    }
    .category {
        color: purple;
        font-weight: bold;
    }
    .score {
        font-size: 1.2rem;
        color: #2980b9;
    }
    </style>
    """, unsafe_allow_html=True)      
        

# Streamlit app
def app():
    st.title("Bulk File Renamer")
    
    # File uploader for multiple files
    uploaded_files = st.file_uploader("Choose files to rename", type=None, accept_multiple_files=True)
    
    if uploaded_files:
        # Create a temporary directory to store uploaded files
        temp_dir = tempfile.mkdtemp()

        # Save uploaded files to the temporary directory
        for uploaded_file in uploaded_files:
            file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
        
        # Get the name pattern and file extension from the user
        name_pattern = st.text_input("Enter name pattern (e.g., 'file')", "file")
        file_extension = os.path.splitext(uploaded_files[0].name)[1]  # Extract the file extension from the first file
        
        if st.button("Rename Files"):
            rename_files(temp_dir, name_pattern, file_extension)
            st.success(f"Files renamed successfully with the pattern '{name_pattern}_<index>{file_extension}'")
            
            # List renamed files
            renamed_files = os.listdir(temp_dir)
            st.write("Renamed Files:")
            for file in renamed_files:
                st.write(file)
                
            # Option to download the renamed files
            for file in renamed_files:
                with open(os.path.join(temp_dir, file), "rb") as f:
                    st.download_button(
                        label=f"Download {file}",
                        data=f,
                        file_name=file
                    )
            
        # Optional: Cleanup temporary directory after processing
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    app()
