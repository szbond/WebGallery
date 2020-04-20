import React from "react"
import Pics from "@/components/pics"
import "@/css/main.css"
import Pages from "@/components/page"
import OrgPic from "@/components/OrgPic"
export default class App extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            page:1,
            picOnshow:"",
            tagsOnshow:[],
            data:{}

        }
    }
    static defalutProps = {}
    componentDidMount(){      
        this.getPage() 
    }
    render(){
        return <div className = "application">
            <OrgPic pic = {this.state.picOnshow} tags = {this.state.tagsOnshow}></OrgPic>
            <div className="sider" onClick = {this.showOrg}>
                <div className="cont"><Pics data= {this.state.data} page = {this.state.page}></Pics></div>
                 <div className="pageSider">
                    <Pages  currentPage = {this.state.page} getValue = {this.onGetPageValue}></Pages>
                <div>
                    </div>
                </div>
               
            </div>
        </div>
    }
    onGetPageValue = (value)=>{
        this.setState({
            page: value
        })
        this.getPage(value)

    }
    getPage(no=1){
        const controller = new AbortController()
        const signal = controller.signal
        let getUrl = "http://localhost:5000/get/page?pageNo=" + no
        fetch(getUrl, {signal})
            .then((res)=>res.json(), err=>alert("get pics fail err: " + err.message))
            .then(body => {
                if (body.length <= 0){
                    return
                }
                let pic = Object.keys(body)[0]
                this.setState({
                    picOnshow:"http://localhost:5000/get/realPic/" +pic ,
                    tagsOnshow:body[pic],
                    page: no,
                    data:body
                })
            })
        setTimeout(()=>controller.abort(), 5000) 
    }
    showOrg=(e)=>{
        if (e.target.className === "pic"){
            console.log(e.target.id)
            this.setState({
                picOnshow: "http://localhost:5000/get/realPic/" + e.target.id,
                tagsOnshow:this.state.data[e.target.id]

                
            })
        }
        
    }
   

}