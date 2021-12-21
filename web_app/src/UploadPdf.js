import axios from "axios";
import React from "react";

export default function UploadPdf() {
  const [selectedFile, setSelectedFile] = React.useState(null);
  const [msg, setMsg] = React.useState('');

  const handleClick = async (event) => {
    setMsg("Proje Yükleniyor")
    event.preventDefault();
    const formData = new FormData();
    formData.append("pdf", selectedFile);
    try {
      const response = await axios({
        headers: {
          "Content-Type": "multipart/form-data",
          "Authorization": "Bearer " + localStorage.getItem("access_token"),
        },
        method: "post",
        url: "http://localhost:8080/api/v1/upload_project",
        data: formData,
      });
      if(response.status===200){
          setMsg("Proje Yüklendi");
      }
      else{
      }
    } catch (error) {
     
      console.log(error);
    }
  };

  const handleFileSelect = (event) => {
    setSelectedFile(event.target.files[0]);
  };
  return (
    <div className="bg-white rounded-lg shadow sm:max-w-md sm:w-full sm:mx-auto sm:overflow-hidden">
      <div className="px-4 py-8 sm:px-10">
        <div className="relative mt-6">
          <div className="absolute inset-0 flex items-center">
            <div className="w-full border-t border-gray-300"></div>
          </div>
          <div className="relative flex justify-center text-sm leading-5">
            <span className="px-2 text-gray-500 bg-white">Pdf Yükle </span>
          </div>
        </div>
        <div className="mt-6">
          <div className="w-full space-y-6">
            <div className="w-full">
              <div className=" relative ">
                <input
                  type="file"
                  id="file"
                  onChange={handleFileSelect}
                  className=" rounded-lg border-transparent flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
                  placeholder="Dosya"
                />
              </div>
            </div>
            <div>
              <span className="block w-full rounded-md shadow-sm">
                <button
                onClick={handleClick}
                  type="button"
                  className="py-2 px-4  bg-indigo-600 hover:bg-indigo-700 focus:ring-indigo-500 focus:ring-offset-indigo-200 text-white w-full transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2  rounded-lg "
                >
                  Yükle
                </button>
                {msg}
              
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
