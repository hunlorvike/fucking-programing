Dưới đây là phiên bản nâng cấp của tài liệu về SignalR, tập trung vào việc xây dựng ứng dụng nhắn tin tương tự Messenger, với các ví dụ chi tiết về cách gửi tin nhắn giữa hai người và trong một nhóm.

## SignalR trong .NET - Ứng Dụng Nhắn Tin Tương Tự Messenger

**SignalR** là một thư viện trong .NET cho phép xây dựng các ứng dụng web thời gian thực, giúp truyền tải dữ liệu giữa máy chủ và client một cách nhanh chóng và hiệu quả. SignalR hỗ trợ nhiều giao thức truyền tải khác nhau, bao gồm WebSockets, Server-Sent Events, và Long Polling.

### Mục lục

1. [Cấu trúc cơ bản của SignalR](#signalr-structure)
2. [Kết nối SignalR](#signalr-connection)
3. [Hub và Communication](#signalr-hub)
4. [Gửi và Nhận tin nhắn cá nhân](#signalr-personal-messaging)
5. [Gửi và Nhận tin nhắn trong nhóm](#signalr-group-messaging)
6. [Quản lý kết nối](#signalr-connection-management)
7. [Xử lý sự kiện và lỗi](#signalr-events)
8. [Chạy SignalR trong ASP.NET Core](#signalr-aspnet-core)

### <a name="signalr-structure"></a>1. Cấu trúc cơ bản của SignalR

SignalR bao gồm các thành phần chính sau:

- **Hubs**: Là điểm giao tiếp giữa client và server, cho phép gọi các phương thức từ client và server dễ dàng.
- **Connections**: Đại diện cho kết nối giữa client và server.
- **Groups**: Cho phép tổ chức các kết nối thành các nhóm để gửi tin nhắn tới một nhóm kết nối cụ thể.

### <a name="signalr-connection"></a>2. Kết nối SignalR

Để kết nối tới một Hub SignalR, client cần sử dụng JavaScript hoặc C#. Dưới đây là ví dụ kết nối bằng JavaScript.

```javascript
const connection = new signalR.HubConnectionBuilder()
  .withUrl('/chatHub')
  .build();

connection
  .start()
  .then(() => {
    console.log('Connected to SignalR hub!');
  })
  .catch(err => console.error(err));
```

### <a name="signalr-hub"></a>3. Hub và Communication

Hub là thành phần trung tâm trong SignalR, cho phép client gọi phương thức trên server và ngược lại. Dưới đây là ví dụ về một Hub cho ứng dụng nhắn tin.

```csharp
using Microsoft.AspNetCore.SignalR;

public class ChatHub : Hub
{
    // Gửi tin nhắn cá nhân đến một người dùng cụ thể
    public async Task SendMessageToUser(string user, string message)
    {
        await Clients.User(user).SendAsync("ReceiveMessage", Context.User.Identity.Name, message);
    }

    // Gửi tin nhắn tới tất cả người dùng trong một nhóm
    public async Task SendMessageToGroup(string groupName, string message)
    {
        await Clients.Group(groupName).SendAsync("ReceiveGroupMessage", Context.User.Identity.Name, message);
    }

    // Tham gia vào một nhóm
    public async Task JoinGroup(string groupName)
    {
        await Groups.AddToGroupAsync(Context.ConnectionId, groupName);
    }

    // Rời khỏi một nhóm
    public async Task LeaveGroup(string groupName)
    {
        await Groups.RemoveFromGroupAsync(Context.ConnectionId, groupName);
    }
}
```

### <a name="signalr-personal-messaging"></a>4. Gửi và Nhận tin nhắn cá nhân

**Gửi tin nhắn từ Client tới một người dùng khác:**

```javascript
function sendMessageToUser() {
  const recipient = 'User2'; // Tên người nhận
  const message = 'Hello, User2!';
  connection
    .invoke('SendMessageToUser', recipient, message)
    .catch(err => console.error(err));
}
```

**Nhận tin nhắn từ Hub:**

```javascript
connection.on('ReceiveMessage', (user, message) => {
  console.log(`Personal message from ${user}: ${message}`);
});
```

### <a name="signalr-group-messaging"></a>5. Gửi và Nhận tin nhắn trong nhóm

**Tham gia vào một nhóm:**

```javascript
function joinGroup() {
  const groupName = 'Friends'; // Tên nhóm
  connection.invoke('JoinGroup', groupName).catch(err => console.error(err));
}
```

**Gửi tin nhắn tới nhóm:**

```javascript
function sendMessageToGroup() {
  const groupName = 'Friends'; // Tên nhóm
  const message = 'Hello, everyone!';
  connection
    .invoke('SendMessageToGroup', groupName, message)
    .catch(err => console.error(err));
}
```

**Nhận tin nhắn từ nhóm:**

```javascript
connection.on('ReceiveGroupMessage', (user, message) => {
  console.log(`Group message from ${user}: ${message}`);
});
```

### <a name="signalr-connection-management"></a>6. Quản lý kết nối

SignalR tự động quản lý kết nối và tái kết nối khi mất kết nối. Tuy nhiên, bạn cũng có thể xử lý các sự kiện kết nối như sau:

```javascript
connection.onreconnecting(err => {
  console.log('Reconnecting...');
});

connection.onreconnected(connectionId => {
  console.log('Reconnected. Connection ID:', connectionId);
});

connection.onclose(err => {
  console.log('Connection closed. Please reload the page.');
});
```

### <a name="signalr-events"></a>7. Xử lý sự kiện và lỗi

SignalR cung cấp một số sự kiện để bạn có thể xử lý các tình huống như mất kết nối, lỗi kết nối và tái kết nối.

- **onreconnecting**: Xảy ra khi SignalR đang cố gắng kết nối lại.
- **onreconnected**: Xảy ra khi SignalR đã kết nối lại thành công.
- **onclose**: Xảy ra khi kết nối đã bị đóng.

### <a name="signalr-aspnet-core"></a>8. Chạy SignalR trong ASP.NET Core

Để sử dụng SignalR trong ứng dụng ASP.NET Core, bạn cần cài đặt gói NuGet `Microsoft.AspNetCore.SignalR`. Sau đó, bạn có thể cấu hình SignalR trong `Startup.cs` như sau:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddSignalR();
}

public void Configure(IApplicationBuilder app, IHostingEnvironment env)
{
    app.UseRouting();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapHub<ChatHub>("/chatHub");
    });
}
```

### Tóm tắt

- **Cấu trúc cơ bản**: SignalR bao gồm Hubs, Connections, và Groups cho phép truyền tải dữ liệu giữa client và server.
- **Gửi và nhận tin nhắn cá nhân**: Hỗ trợ gửi và nhận tin nhắn giữa hai người dùng.
- **Gửi và nhận tin nhắn trong nhóm**: Cho phép gửi và nhận tin nhắn tới tất cả người dùng trong một nhóm.
- **Quản lý kết nối**: SignalR tự động quản lý kết nối và cho phép xử lý các sự kiện kết nối.
- **Chạy trong ASP.NET Core**: Cần cấu hình trong `Startup.cs` và cài đặt gói NuGet để sử dụng.

SignalR là một công cụ mạnh mẽ giúp phát triển các ứng dụng thời gian thực, cải thiện trải nghiệm người dùng thông qua việc truyền tải dữ liệu nhanh chóng và hiệu quả, đặc biệt trong các ứng dụng nhắn tin.
