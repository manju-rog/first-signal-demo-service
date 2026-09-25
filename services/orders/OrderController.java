package demo.orders;

public class OrderController {
  private final OrderHandler handler = new OrderHandler();

  public String submit(String payload) {
    return handler.handle(payload);
  }
}
