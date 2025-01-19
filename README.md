Title: Online Store
Description: This system allows customers to buy any product of their choice online.
Class Diagram:
        +-----------------------+
        |   Online Store        |
        |                       |
        |   +--------------+    |
        |   | Browse      |    |
        |   | Products    |    |
        |   +--------------+    |
        |   +--------------+    |
        |   | Add to Cart  |    |
        |   +--------------+    |
        |   +--------------+    |
        |   | Place Order  |    |
        |   +--------------+    |
        |                       |
        |   +----------------+  |
        |   | Manage Users   |  |
        |   +----------------+  |
        +-----------------------+
             /         \
        Customer    Administrator
