import React from "react"
import{Tag} from "antd"
export default class OrgPic extends React.Component{
    constructor(props){
        super(props)
        this.state = {  
        }
    }
    render(){
        console.log(this.props.pic)
        return  <div className="view">
                    <div className = "view-img">
                    <div className="img-cont">
                    <img src={this.props.pic} alt="org" id = "org"/>
                    <div className="img-tags">
                    {this.props.tags.map(tag=><Tag key={tag} closable>{tag}</Tag>)}
                </div>
                </div>                  
            </div>
        </div>
    }
}