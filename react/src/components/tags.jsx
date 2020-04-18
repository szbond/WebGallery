import React from "react"

export default class Pics extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            data:[]
            
        }
    }
    static defalutProps = {}
    /*
    componentWillMount(){
        const controller = new AbortController()
        const signal = controller.signal
        let getUrl = "http://localhost:5000/get/tags" + "?pic=" + this.props.pic 
        fetch(getUrl, {signal})
            .then((res)=>res.json(), err=>alert("get tags fail err: " + err.message))
            // .then(res => res.json() )
            .then(body => {
                let tags = []
                this.setState({
                    data: tags
                })
            })
            // .catch(err => console.error(err))
        setTimeout(()=>controller.abort(), 5000) 
    }
    */
   
    render(){
        return <div>
            <div className = "tags">{this.props.tags.join(" ")}</div>   
        </div>
    }
}