pragma solidity ^0.8.0;

contract FirstContract {

    string public message;

    constructor(string memory initMessage) public {
        message = initMessage;
    }

    function updateMessage(string memory newMessage) public {
        message = newMessage;
    }

    function getMessage() public view returns (string memory) {
        return message;
    }
}
