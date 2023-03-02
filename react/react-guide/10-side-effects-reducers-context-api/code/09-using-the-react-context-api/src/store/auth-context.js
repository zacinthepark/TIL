import React from 'react';

// context는 대부분 객체
const AuthContext = React.createContext({
  isLoggedIn: false
});

export default AuthContext;