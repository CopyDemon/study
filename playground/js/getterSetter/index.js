
class Test{
    constructor(){
        console.log(`class is loaded`)
    }

    get text(){
        console.log(`text`)
    }

    set text(newText){
        console.log(newText)
    }
}

const myTest = new Test();
myTest.text
myTest.text = "asd"
