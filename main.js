// enter whatsapp web and select the group

// make sure there are no contacts in the 'chat' section (you can do it by filtering the chats)

// put it in the developer's console

let members = document.querySelectorAll('span[title^="+"]');

let contacts = [];

members.forEach(member => {
  contacts.push(member.getAttribute('title'));
});

console.log(contacts);

// save the info