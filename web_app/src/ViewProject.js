import axios from "axios";
import React from "react";
import {useParams} from 'react-router-dom';

export default function ViewProject(){
    const [project, setProject] = React.useState({
        "advisor": {
            "advisor_degree": "",
            "advisor_name": "",
            "advisor_surname": ""
        },
        "author": {
            "education_type": "",
            "id": null,
            "name_surname": "",
            "student_no": null
        },
        "document_id":null,
        "jury": {
            "jury_degree": "",
            "jury_name": "",
            "jury_surname": ""
        },
        "lesson_type": "",
        "p_delivery": "",
        "p_keywords": "",
        "p_summary": "",
        "p_title": "",
        "project_id": null,
        "user_id": null
    });
    let params = useParams();
    var config = {
        method: 'get',
        url: "http://localhost:8080/api/v1/project/"+params.id,
        headers: { 
          'Authorization': 'Bearer '+localStorage.getItem('access_token'),
        }
      };
      
      axios(config)
      .then(function (response) {
        setProject(response.data)
      })
      .catch(function (error) {
        console.log(error);
      });
    return(
        <div>
       
        <div className="bg-white max-w-full shadow overflow-hidden sm:rounded-lg">
            <div className="px-4 py-5 sm:px-6">
                <h3 className="text-lg leading-6 font-medium text-gray-900">
                    {project.p_title}
                </h3>
                <p className="mt-1 max-w-2xl text-sm text-gray-500">
                    {project.p_summary}
                </p>
            </div>
            <div className="border-t border-gray-200">
                <dl>
                    <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt className="text-sm font-medium text-gray-500">
                            Anahtar Kelimeler
                        </dt>
                        <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                           {project.p_keywords}
                        </dd>
                    </div>
                    <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt className="text-sm font-medium text-gray-500">
                            Ders Tipi
                        </dt>
                        <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                           {project.lesson_type}
                        </dd>
                    </div>
                    <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt className="text-sm font-medium text-gray-500">
                           Juri
                        </dt>
                        <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                          <p> İsim : {project.jury['jury_name']} { project.jury['jury_surname']} </p>
                          <p> Derecesi : {project.jury['jury_degree']}  </p>
                        </dd>
                    </div>
                    <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt className="text-sm font-medium text-gray-500">
                           Yazar
                        </dt>
                        <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                          <div> <p className="mt-1 text-lg text-gray-900">İsim</p> {project.author['name_surname']} </div>
                          <div> <p className="mt-1 text-lg text-gray-900">Öğrenci Numarası</p> {project.author['student_no']} </div>
                          <div> <p className="mt-1 text-lg text-gray-900">Öğretim Türü</p> {project.author['education_type']} </div>
                        </dd>
                    </div>
                    <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt className="text-sm font-medium text-gray-500">
                           Danışman
                        </dt>
                        <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                          <div> <p className="mt-1 text-lg text-gray-900">Ad Soyad</p> {project.advisor['advisor_name']} </div>
                          <div> <p className="mt-1 text-lg text-gray-900">Unvan</p> {project.advisor['advisor_degree']} </div>
                        </dd>
                    </div>
                </dl>
            </div>
        </div>
        </div>
        )
}