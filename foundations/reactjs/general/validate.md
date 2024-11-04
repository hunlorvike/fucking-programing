Trong React, có nhiều cách để thực hiện **validate form** (xác thực biểu mẫu), từ các giải pháp thủ công với **state** đến việc sử dụng các thư viện như **Formik**, **React Hook Form**, hoặc **Yup** để giảm thiểu mã lặp lại. Dưới đây là các phương pháp phổ biến:



## 1. Sử Dụng **State** và **Event Handlers** Để Tự Xác Thực

Với phương pháp này, bạn sẽ dùng các **hooks** (`useState`, `useEffect`) để quản lý các giá trị và lỗi của form.

### Cách làm:

- Tạo `state` cho từng trường input.
- Sử dụng `onChange` để cập nhật `state` và kiểm tra tính hợp lệ của dữ liệu.
- Khi submit, kiểm tra lại tất cả các trường để đảm bảo form hợp lệ.

```javascript
import React, { useState } from 'react';

function SimpleForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({});

  const validate = () => {
    const newErrors = {};
    if (!email.includes('@')) newErrors.email = 'Email không hợp lệ';
    if (password.length < 6)
      newErrors.password = 'Mật khẩu phải có ít nhất 6 ký tự';
    return newErrors;
  };

  const handleSubmit = event => {
    event.preventDefault();
    const newErrors = validate();
    setErrors(newErrors);
    if (Object.keys(newErrors).length === 0) {
      console.log('Form hợp lệ, thực hiện đăng nhập');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Email:</label>
        <input
          type="text"
          value={email}
          onChange={e => setEmail(e.target.value)}
        />
        {errors.email && <p>{errors.email}</p>}
      </div>
      <div>
        <label>Mật Khẩu:</label>
        <input
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
        {errors.password && <p>{errors.password}</p>}
      </div>
      <button type="submit">Đăng nhập</button>
    </form>
  );
}
```



## 2. Sử Dụng **React Hook Form**

**React Hook Form** là một thư viện phổ biến trong React giúp quản lý form với API đơn giản và hiệu quả. React Hook Form hỗ trợ giảm thiểu re-render không cần thiết và tích hợp dễ dàng với các thư viện xác thực như **Yup**.

### Cách làm:

1. Cài đặt thư viện:

   ```bash
   npm install react-hook-form
   ```

2. Sử dụng `useForm` từ React Hook Form để quản lý form.

```javascript
import React from 'react';
import { useForm } from 'react-hook-form';

function HookForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = data => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label>Email:</label>
        <input
          type="text"
          {...register('email', {
            required: 'Vui lòng nhập email',
            pattern: /^[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/,
          })}
        />
        {errors.email && <p>{errors.email.message}</p>}
      </div>
      <div>
        <label>Mật Khẩu:</label>
        <input
          type="password"
          {...register('password', {
            required: 'Vui lòng nhập mật khẩu',
            minLength: {
              value: 6,
              message: 'Mật khẩu phải có ít nhất 6 ký tự',
            },
          })}
        />
        {errors.password && <p>{errors.password.message}</p>}
      </div>
      <button type="submit">Đăng nhập</button>
    </form>
  );
}
```



## 3. Kết Hợp **React Hook Form** và **Yup** để Xác Thực Schema

**Yup** là thư viện giúp xây dựng schema xác thực cho form một cách dễ dàng, và kết hợp tốt với React Hook Form để tạo các form phức tạp.

1. Cài đặt **Yup** và **@hookform/resolvers** để tích hợp Yup với React Hook Form:

   ```bash
   npm install yup @hookform/resolvers
   ```

2. Tạo schema xác thực với Yup và dùng `yupResolver` để tích hợp schema vào React Hook Form.

```javascript
import React from 'react';
import { useForm } from 'react-hook-form';
import * as yup from 'yup';
import { yupResolver } from '@hookform/resolvers/yup';

// Định nghĩa schema Yup
const schema = yup.object().shape({
  email: yup
    .string()
    .email('Email không hợp lệ')
    .required('Vui lòng nhập email'),
  password: yup
    .string()
    .min(6, 'Mật khẩu phải có ít nhất 6 ký tự')
    .required('Vui lòng nhập mật khẩu'),
});

function FormWithYup() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(schema),
  });

  const onSubmit = data => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label>Email:</label>
        <input type="text" {...register('email')} />
        {errors.email && <p>{errors.email.message}</p>}
      </div>
      <div>
        <label>Mật Khẩu:</label>
        <input type="password" {...register('password')} />
        {errors.password && <p>{errors.password.message}</p>}
      </div>
      <button type="submit">Đăng nhập</button>
    </form>
  );
}
```



## 4. Sử Dụng **Formik** và **Yup**

**Formik** là một thư viện giúp đơn giản hóa quá trình quản lý form và xác thực trong React. Khi kết hợp với **Yup**, Formik giúp xây dựng các form phức tạp với mã lệnh gọn gàng.

1. Cài đặt **Formik** và **Yup**:

   ```bash
   npm install formik yup
   ```

2. Sử dụng Formik với Yup để xác thực.

```javascript
import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as yup from 'yup';

// Định nghĩa schema Yup
const schema = yup.object().shape({
  email: yup
    .string()
    .email('Email không hợp lệ')
    .required('Vui lòng nhập email'),
  password: yup
    .string()
    .min(6, 'Mật khẩu phải có ít nhất 6 ký tự')
    .required('Vui lòng nhập mật khẩu'),
});

function FormikForm() {
  const initialValues = { email: '', password: '' };

  const onSubmit = values => {
    console.log(values);
  };

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={schema}
      onSubmit={onSubmit}
    >
      <Form>
        <div>
          <label>Email:</label>
          <Field type="text" name="email" />
          <ErrorMessage name="email" component="p" />
        </div>
        <div>
          <label>Mật Khẩu:</label>
          <Field type="password" name="password" />
          <ErrorMessage name="password" component="p" />
        </div>
        <button type="submit">Đăng nhập</button>
      </Form>
    </Formik>
  );
}

export default FormikForm;
```



## Kết Luận

- **State và Event Handlers** phù hợp với các form nhỏ, đơn giản.
- **React Hook Form** giúp quản lý form dễ dàng và tối ưu cho hiệu suất, rất phù hợp khi muốn kiểm soát form phức tạp mà vẫn giảm thiểu re-render.
- **Formik** với Yup là một lựa chọn mạnh mẽ khi làm việc với các form lớn, phức tạp, hỗ trợ tốt xác thực schema.
