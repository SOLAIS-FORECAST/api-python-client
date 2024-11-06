.. _configuration:

Configuration
=============

Calibsunapi requires little to no configuration to work, depending on if you're using demo endpoints or real endpoints.


Demo endpoints
--------------

In this case, no configuration is required. You can start using the client right away.

Real endpoints
--------------

In this case, you need to authenticate with the Calibsun API. You can do this by setting the following environment variables:

- `CALIBSUN_CLIENT_ID`: Your Calibsun api key id
- `CALIBSUN_CLIENT_SECRET`: Your Calibsun api key secret

To get your api key id and secret, access you profile in your calibsun account and generate a credential pair in [your account settings](https://www.calibsun.com/en/dashboard/api).
You can regenerate your credentials at any time, but be careful, the previous credential are then immediately revoked.

All the plants created from your account are directly accessible from the client.
If you want to access plants owned by another account, the owner must send a request to the Calibsun support team to grant you access to their plants.