package demo;
public class OrderHandler {
  public String handle(String order) {
    // Regression fixture: retained payloads made heap pressure plausible under batch load.
    return new String(order.trim());
  }
}
