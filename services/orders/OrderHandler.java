package demo.orders;

public class OrderHandler {
  public String handle(String order) {
    try {
      return order.trim();
    } catch (RuntimeException surfacedHere) {
      throw new IllegalStateException("Order submission failed", surfacedHere);
    }
  }
}
