import Login from "./Login";
import Users from "./Users";
import Footer from "./Footer";
import Header from "./Header";
import UploadPdf from "./UploadPdf";
import { Routes, Route } from "react-router-dom";
import UserManagmenet from "./UserManagement";
import ViewProject from "./ViewProject";
import ProjectLİst from './ProjectList'

export default function App() {
  return (
    <div>
       <Header/>
      <div className="container  max-w-screen-lg mx-auto">
        <div class="py-8">
          <Routes>
           <Route path="/" element={<UploadPdf />} />
            <Route path="/login" element={<Login />} />
            <Route path="/users" element={<Users />} />
            <Route path="/add_user" element={<UserManagmenet />} />
            <Route path="/upload_pdf" element={<UploadPdf />} />
            <Route path="/project_list" element={<ProjectLİst/>} />
            <Route path="/view_project/:id" element={<ViewProject/>}/>
          </Routes>
        </div>
      </div>
      <Footer />
    </div>
  );
}
