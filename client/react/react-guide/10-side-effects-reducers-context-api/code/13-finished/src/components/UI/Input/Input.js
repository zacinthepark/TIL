import React, { useRef, useImperativeHandle } from 'react';

import classes from './Input.module.css';

// ref 인자는 함수형 컴포넌트의 외부에서 ref를 설정해야 하는 경우 바인딩을 형성하는 부분
// ref라는 두번째 인수를 활성화시키려면 컴포넌트 함수를 특별한 방법으로 export할 필요가 있음
// React.forwardRef()로 감싸줘야함
// forwardRef()의 반환값은 리액트 컴포넌트이며, Input은 이제 ref에 바인딩 될 수 있는 리액트 컴포넌트가 됨
const Input = React.forwardRef((props, ref) => {
  const inputRef = useRef();

  const activate = () => {
    inputRef.current.focus();
  };

  // 첫번째 인자는 ref
  // 두번째 인자는 객체를 반환하는 함수
  // 반한되는 객체에는 외부에서 사용할 수 있는 모든 데이터를 포함할 것 (키는 외부에서 사용할 이름, 값은 참조하는 내부값)
  useImperativeHandle(ref, () => {
    return {
      focus: activate,
    };
  });

  return (
    <div
      className={`${classes.control} ${
        props.isValid === false ? classes.invalid : ''
      }`}
    >
      <label htmlFor={props.id}>{props.label}</label>
      <input
        ref={inputRef}
        type={props.type}
        id={props.id}
        value={props.value}
        onChange={props.onChange}
        onBlur={props.onBlur}
      />
    </div>
  );
});

export default Input;
