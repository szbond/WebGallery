import React from "react"
import Pic from "@/components/pic"
export default class Pics extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            pageNo:1,
            data:{}
            // 查询结果 '["a", "b"]'
            // data:JSON.parse('["src/images/IMG_2020011811_3010_0790.jpg", "src/images/IMG_2020011811_3010_0791.jpg"]')
        }
    }
    static defalutProps = {}
    UNSAFE_componentWillMount(){
        this.getPage()
    }
    render(){
        console.log(typeof(this.state.data))
        let pics = Object.getOwnPropertyNames(this.state.data)
        return <div>
            {pics.map(pic=>{
                return <Pic key = {pic} name = {pic} tags = {this.state.data[pic]}></Pic>
            })}
            <div><input type="button" value = "next page" onClick = {()=>{
                let newPage = this.state.pageNo + 1
                console.log(newPage)
                this.getPage(newPage)
                this.setState({
                    pageNo: newPage
                })
                
            }}/></div>   
        </div>
    }
    getPage(no=1){
        const controller = new AbortController()
        const signal = controller.signal
        let getUrl = "http://localhost:5000/get/page?pageNo=" + no
        fetch(getUrl, {signal})
            .then((res)=>res.json(), err=>alert("get pics fail err: " + err.message))
            // .then(res => res.json() )
            .then(body => {
                
                this.setState({
                    data: body
                })
            })
            // .catch(err => console.error(err))
        setTimeout(()=>controller.abort(), 5000) 
    }
}