import React from "react"
import Pics from "@/components/pics"
import Pagination from "antd"
// import Page from "@/components/page"
export default class App extends React.Component{
    constructor(props){
        super(props)
        this.state = {

        }
    }
    static defalutProps = {}
    render(){
        return <div>
            <h1>gallery</h1>
            <div className = "org">
                <img src="" alt="org" id = "org"/>
            </div>
            <Pics></Pics>
            {/* <Pagination total = {5}/> */}
            
        </div>
    }
}