import Login from "./Login";
import Users from "./Users";
import Footer from "./Footer";
import Header from "./Header";
import UploadPdf from "./UploadPdf";
import ViewPdf from "./ViewPdf";
import { Routes, Route, Link } from "react-router-dom";
import UserManagmenet from "./UserManagement";
import ViewProject from "./ViewProject";

export default function App() {
  return (
    <div>
      
      <div className="container  max-w-screen-lg mx-auto">
        <div class="py-8">
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/users" element={<Users />} />
            <Route path="/add_user" element={<UserManagmenet />} />
            <Route path="/upload_pdf" element={<UploadPdf />} />
            <Route path="/view_pdf" element={<ViewPdf/>} />
            <Route path="/view_project/:id" element={<ViewProject/>}/>
          </Routes>
        </div>
      </div>
      <Footer />
    </div>
  );
}
