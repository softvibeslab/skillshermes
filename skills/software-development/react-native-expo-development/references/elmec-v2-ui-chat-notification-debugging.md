# ELMEC V2 UI, chat, and notification debugging

This reference preserves codebase-specific fixes from an Expo + Supabase application. Adapt paths, schema names, and role values rather than treating them as universal Expo conventions.

## Unread badge does not decrease from request details

Observed behavior: opening a request did not reduce the Chat-tab badge, while entering the chat route did.

Root cause: the chat route marked messages read, but request-detail navigation bypassed that lifecycle. The badge also depended on related unread rows in a `notifications` table.

Known pattern in `app/(tabs)/requests.tsx`:

1. Find the room associated with the request.
2. Await the shared `markMessagesAsRead(roomId)` mutation.
3. Mark matching `new_message` notification rows read for the current user.
4. Do not block navigation if notification cleanup fails, but log the error.
5. Re-read or observe the authoritative unread counter after mutation.

Example shape:

```tsx
const chatRoom = chatRooms.find(room => room.request_id === request.id);
if (chatRoom) {
  await markMessagesAsRead(chatRoom.id);
  try {
    await supabaseClient
      .from('notifications')
      .update({ read: true })
      .match({ user_id: user?.id, type: 'new_message', read: false })
      .contains('data', {
        notification_event_key: `new_message:${chatRoom.id}:`,
      });
  } catch (error) {
    console.error('Failed to mark notifications as read:', error);
  }
}
```

Verify the exact `.contains(...)` semantics and stored JSON shape in the live schema; a prefix-like event string inside JSON may not behave as expected on every implementation.

## Missing create-request floating action button

Observed behavior: the Requests-tab FAB was absent.

Root cause: rendering was gated by `user?.rol === 'customer'`.

Debug by logging the loaded profile role and checking the corresponding Supabase row. A temporary unconditional render can isolate the gate, but label and revert it after diagnosis. The durable fix should correct profile data or the intended authorization policy, not leave the UI bypassed.

## Chat tab missing or untappable

Observed behavior: the icon was absent or disabled.

Root cause: `chatTabEnabledByRole` in `app/(tabs)/_layout.tsx` mapped the relevant roles to `false`.

Update only roles intended to access chat, then test each role and ensure route-level authorization agrees with tab visibility. Showing a tab is not a substitute for backend or route authorization.

## General lesson

When several entry points represent the same domain action (open request, open chat, tap notification), centralize read-state mutation or call the same domain function from every entry point. Derived badges should have one documented source of truth, or every contributing store must be updated and verified together.
