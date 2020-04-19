import React from "react"
import Tag from "@/components/tags"
export default class Pic extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            name:this.props.name,
            showTags:props.tags

        }
        // 提交缓存
        this.tags = ""
    }
    static defalutProps = {}
    render(){
        // console.log(this.props.tags)
        return <div className = "pic-cont">
            <img className = "pic" src={"http://localhost:5000/static/images/thumb/" + this.props.name} alt="pic" onClick = {()=>{this.showOrg()}}/>
            <br/>
            <p>{this.state.name}</p>
            
            <input type="text" value = {this.state.showTags.join(" ") } readOnly/>
            <br/>
            <input type="text" placeholder="tags" id = {this.state.name} onChange={()=>{this.saveTags()}}/>
            <br/>
            <input type="button" value = "submit" onClick={()=>{this.submTags()}}/>
            {/* <Tag tags = {this.props.tags}></Tag>   */}
            {/* <input type="button" value="show" onClick = {()=>{this.showOrg()}}/> */}
            
    
        </div>
    }
    saveTags(){
        let tagInput = document.getElementById(this.state.name)
        this.tags = tagInput.value      
    }
    submTags(){
        
        let newTags = []
        this.tags.split(" ").map(tag=>{
            if (tag.length > 0 && newTags.indexOf(tag) == -1){
                newTags.push(tag)
            }
        })             
        const controller = new AbortController()
        const signal = controller.signal
        let getUrl = "http://localhost:5000/submit/tags" + "?pic=" + this.state.name + "&tags=" + JSON.stringify(newTags) 
        fetch(getUrl, {signal})
            .then((res)=>res.json(), err=>alert("submit fail err: " + err.message))
            // .then(res => res.json() )
            .then(body => {
                this.joinTags(body)
            })
            // .catch(err => console.error(err))
        setTimeout(()=>controller.abort(), 5000)
    }
    joinTags(tags){
        let newTags = this.state.showTags
        JSON.parse(tags).map(tag=>{
            if (newTags.indexOf(tag) == -1){
                newTags.push(tag)
            }         
        })
        this.setState({
            showTags: newTags
        })

    }
    showOrg(){
        let img = document.getElementById("org")
        img.setAttribute("src", "http://localhost:5000/get/realPic/" + this.state.name)
    }
    
}