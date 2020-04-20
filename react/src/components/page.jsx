import { Pagination } from "antd";
import React from "react"

export default class Pages extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            page:1,
            maxPage: 1

            
        }
    }
    UNSAFE_componentWillMount(){
        this.getMaxPage()
    }
    UNSAFE_componentWillReceiveProps(nextProps){
        if (nextProps.currentPage < this.state.maxPage){
            
            this.setState({
                page: nextProps.currentPage
            })
        }
        if (nextProps.currentPage === this.state.maxPage){
            this.setState({
                maxPage: nextProps.currentPage + 1
             })
            this.getMaxPage()
        }

    }

    render(){
        return <div>
            <Pagination defaultCurrent= {this.state.page} pageSize = {1} total={this.state.maxPage} size="small"  onChange={current=>{
                this.props.getValue(current)
            } }/>
        </div>
    }
    turnPage(pageNo){
        this.getMaxPage()
        if (pageNo > this.state.maxPage){
            return
        }
        this.setState({
            page:pageNo
        })
    }
    getMaxPage(){
        fetch("http://localhost:5000/")
            .then(res=>res.text())
            .then(body=>{
                this.setState({
                    maxPage:parseInt(body) + 1
                })
            })
    }
    
}