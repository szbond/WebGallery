import React from "react"
import Pics from "@/components/pics"
import "@/css/main.css"
import { Layout } from 'antd';

const { Header, Footer, Sider, Content } = Layout;
// import Page from "@/components/page"
export default class App extends React.Component{
    constructor(props){
        super(props)
        this.state = {

        }
    }
    static defalutProps = {}
    render(){
        return <div className = "application">
            <div className="view">
               
                <div className = "view-img">
                    <div className="img-cont"><img src="" alt="org" id = "org"/></div>
                    
                </div>
                
            </div>
            <div className="cont">
                <Pics></Pics>
            </div>
            
            {/* <img src="" alt="org" id = "org"/> */}
            {/* <Pics></Pics> */}
            {/* <Pagination total = {5}/> */}
            
        </div>
    }
}