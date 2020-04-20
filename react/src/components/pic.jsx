import React from "react"
import {Input, Tag} from "antd"
export default class Pic extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            name:this.props.name,
            showTags:props.tags

        }
    }
    static defalutProps = {}
    UNSAFE_componentWillMount(){
        if (this.props.show)(this.showOrg())
    }
    render(){

        return <div className = "pic-cont">
            <img className = "pic" src={"http://localhost:5000/static/images/thumb/" + this.props.name} id={this.props.name} alt="pic" />
            <br/>
            <p>{this.state.name.split(".")[0]}</p>
            
            {this.state.showTags.map(tag=><Tag closable onClose={()=>this.tagClose(tag)} key = {tag}>{tag}</Tag>)}
            <br/>
            <Input placeholder="input tags here" allowClear onPressEnter={(e)=>{this.submTags(e)}}/>
        
    
        </div>
    }
    submTags(e){

        let Tags = []
        e.target.value.split(" ").map(tag=>{
            if (tag.length > 0 && Tags.indexOf(tag) == -1){
                Tags.push(tag)
            }
        })             
        const controller = new AbortController()
        const signal = controller.signal
        let getUrl = "http://localhost:5000/submit/tags" + "?pic=" + this.state.name + "&tags=" + JSON.stringify(Tags) 
        fetch(getUrl, {signal})
            .then((res)=>res.json(), err=>alert("submit fail err: " + err.message))
            .then(body => {
                this.joinTags(body)
            })

        setTimeout(()=>controller.abort(), 5000)
    }
    joinTags(tags){
        let newTags = this.state.showTags
        JSON.parse(tags).map(tag=>{
            if (newTags.indexOf(tag) == -1){
                console.log(tag)
                newTags.push(tag)
            }         
        })
        this.setState({
            showTags: newTags
        })

    }
    tagClose(tag){
        this.state.showTags.splice(this.state.showTags.indexOf(tag), 1)
        console.log(this.state.showTags)
    }
    showOrg(){
        let img = document.getElementById("org")
        img.setAttribute("src", "http://localhost:5000/get/realPic/" + this.state.name)
        let tags = document.getElementById("orgTags")
        tags.innerHTML = this.state.showTags.join(" ")
    }
    
}