pragma solidity ^0.5.0;

contract AssociateProfitSplitter { // Contract definition
   
    address payable public employee_one; // Declares employee_one as public payable address
    address payable public employee_two; // Declares employee_two as public payable address
    address payable public employee_three; // Declares employee_three as public payable address

    constructor(address payable _one, address payable _two, address payable _three) public { //Constructor defintion
        employee_one = _one; // Sets employee_one variable to parameter _one address
        employee_two = _two; // Sets employee_two variable to parameter _two address
        employee_three = _three; // Sets employee_three variable to parameter _three address
    }

    function balance() public view returns(uint) { // Balance function defintion
        return address(this).balance; // Returns balance of contract, should always be 0
    }

    function deposit() public payable { // Payable function defintion
        uint amount = msg.value / 3; // Splits `msg.value` into three and sets amount = to it

        employee_one.transfer(amount); // Transfers the amount to employee_one
        employee_two.transfer(amount); // Transfers the amount to employee_two
        employee_three.transfer(amount); // Transfers the amount to employee_three
        msg.sender.transfer(msg.value - amount * 3); // Takes care of a potential remainder by sending back to msg.sender
    }

    function() external payable { // Fallback function definition
        deposit(); // Calls the deposit function
    }
}