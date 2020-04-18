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
        // console.log("ren")
        return <div>
            <img src={"http://localhost:5000/static/images/thumb/" + this.props.name} alt="pic"/>
            <br/>
            <p>{this.state.name}</p>
            
   
            <input type="text" placeholder="tags" id = {this.state.name} onChange={()=>{this.saveTags()}}/>
            <input type="button" value = "submit" onClick={()=>{this.submTags()}}/>
            {/* <Tag tags = {this.props.tags}></Tag>   */}
            <p>{this.state.showTags.join(" ")}</p>
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
    
}