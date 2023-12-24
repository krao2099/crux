import Home from "./home/home";
import {BrowserRouter,Routes,Route,Navigate,Outlet} from "react-router-dom";
import Admin from "./admin/admin";
import Error from "./error/error";

const PrivateRoutes = () => {
  let auth = fetch('https://api.example.com/data');
  console.log(auth);
return (
    auth.Admin ? <Outlet/> : <Navigate to='/error'/>
  )
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/error" element={<Error/>} />
        <Route element={<PrivateRoutes/>}>
          <Route path="/admin" element={<Admin/>} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
