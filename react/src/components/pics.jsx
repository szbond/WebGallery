import React from "react"
import Pic from "@/components/pic"
export default class Pics extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            }
    }
    render(){
        let pics = Object.keys(this.props.data) 
       
        return <div className = "Pics-cont" >
            {/* {this.props.pics.map((pic, index)=>{
                return <Pic key = {pic} name = {pic} tags = {this.props.tags[index]}></Pic>
            })} */}

            {pics.map(pic=>{return <Pic key = {pic} name = {pic} tags = {this,this.props.data[pic]}></Pic>})} 
            
        </div>
    }

   
}