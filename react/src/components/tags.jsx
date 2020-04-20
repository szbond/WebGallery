import React from "react"
import {Tag} from "antd"
export default class Pics extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            tags:[]
            
        }
    }
    static defalutProps = {}
    
    render(){
        return <div>
            <div className = "tags">{this.props.tags.join(" ")}</div>   
        </div>
    }
}