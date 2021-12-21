import Login from "./Login";
import Footer from "./Footer";
import Header from "./Header";
import UploadPdf from "./UploadPdf";
import { Routes, Route } from "react-router-dom";
import NewUser from "./NewUser";
import ViewProject from "./ViewProject";
import ProjectList from './ProjectList';
import UserList from './UserList';
import EditUser from './EditUser';
import Home from "./Home";
export default function App() {
  return (
    <div >
       <Header/>
      <div className="container  max-w-screen-lg mx-auto ">
        <div class="py-8  ">
          <Routes>
           <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/add_user" element={<NewUser />} />
            <Route path="/upload_pdf" element={<UploadPdf />} />
            <Route path="/project_list" element={<ProjectList/>} />
            <Route path="/user_list" element={<UserList/>} />
            <Route path="/edit_user/:id" element={<EditUser/>} />
            <Route path="/view_project/:id" element={<ViewProject/>}/>
          </Routes>
        </div>
      </div>
      <Footer />
    </div>
  );
}
